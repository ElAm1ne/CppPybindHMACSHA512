#include <pybind11/pybind11.h>
#include <hmac.hpp>

namespace py = pybind11;

PYBIND11_MODULE(hmac_cpp, m) {
    m.doc() = "pybind11 hmac_cpp plugin"; 

    py::enum_<hmac::TypeHash>(m, "TypeHash")
        .value("SHA256", hmac::TypeHash::SHA256)
        .value("SHA512", hmac::TypeHash::SHA512)
        .export_values();

    m.def("get_hmac", &hmac::get_hmac, "A function that computes HMAC",
          py::arg("key"),
          py::arg("msg"),
          py::arg("type"),
          py::arg("is_hex") = true,
          py::arg("is_upper") = false);
}
