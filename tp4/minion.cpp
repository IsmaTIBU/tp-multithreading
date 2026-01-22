#include "task.hpp"
#include <cpr/cpr.h>
#include <iostream>
#include <thread>

int main() {
    // Definimos la dirección como 'url'
    const std::string url = "http://localhost:8000";
    std::cout << "Minion prêt à travailler..." << std::endl;

    while (true) {
        auto resp = cpr::Get(cpr::Url{url + "/task_queue"});
        if (resp.status_code == 200 && !resp.text.empty()) {
            json data = json::parse(resp.text);

            if (!data.is_null()) { 
                Task job = Task::from_json(data);
                std::cout << "Execución de la tâche : " << job.identifier << std::endl;
                job.work();

                json result_data = job.to_json();
                
                cpr::Post(cpr::Url{url + "/result_queue"},
                        cpr::Body{result_data.dump()},
                        cpr::Header{{"Content-Type", "application/json"}});
            } else {
                std::this_thread::sleep_for(std::chrono::milliseconds(500));
            }
        } else {
            std::this_thread::sleep_for(std::chrono::milliseconds(500));
        }
    }
    return 0;
}