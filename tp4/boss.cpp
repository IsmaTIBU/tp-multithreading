#include "task.hpp"
#include <cpr/cpr.h>
#include <iostream>
#include <thread>

int main() {
    const std::string url = "http://localhost:8000";
    
    for (int i = 0; i < 10; ++i) {
        Task t(i, 300);
        std::cout << "Boss envoie la tâche " << i << std::endl;
        cpr::Post(cpr::Url{url + "/task_queue"}, 
                  cpr::Body{t.to_json().dump()},
                  cpr::Header{{"Content-Type", "application/json"}});
    }

    int received = 0;
    while (received < 10) {
        auto resp = cpr::Get(cpr::Url{url + "/result_queue"});
        
        if (resp.status_code == 200 && !resp.text.empty()) {
            json data = json::parse(resp.text);

            if (!data.is_null()) {
                Task completed_task = Task::from_json(data);
                std::cout << "Résultat validé : Tâche " << completed_task.identifier
                        << " traitée en " << completed_task.time << "s" << std::endl;
                
                received++; 
            } else {
                std::this_thread::sleep_for(std::chrono::milliseconds(500));
            }
        } else {
            std::this_thread::sleep_for(std::chrono::milliseconds(500));
        }
    }
    std::cout << "Toutes les taches on été traitées" << std::endl;
    return 0;
}