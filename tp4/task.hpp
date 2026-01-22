#pragma once
#include <Eigen/Dense>
#include <chrono>
#include <nlohmann/json.hpp>
#include <vector>

using json = nlohmann::json;

class Task {
public:
    int identifier;
    int size;
    Eigen::MatrixXd a;
    Eigen::VectorXd b;
    Eigen::VectorXd x;
    double time;

    Task(int id = 0, int s = 0) : identifier(id), size(s), time(0.0) {
        if (size > 0) {
            a = Eigen::MatrixXd::Random(size, size);
            b = Eigen::VectorXd::Random(size);
            x = Eigen::VectorXd::Zero(size);
        }
    }

    void work() {
        auto start = std::chrono::steady_clock::now();
        x = a.householderQr().solve(b); // Matrix solving logic
        auto end = std::chrono::steady_clock::now();
        std::chrono::duration<double> diff = end - start;
        time = diff.count();
    }

    json to_json() const {
        return json{{"identifier", identifier}, {"size", size}, {"time", time}};
    }

    static Task from_json(const json& j) {
        Task t(j.at("identifier").get<int>(), j.at("size").get<int>());
        t.time = j.at("time").get<double>();
        return t;
    }
};