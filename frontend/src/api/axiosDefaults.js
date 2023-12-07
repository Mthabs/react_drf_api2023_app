import axios from "axios";

//axios.defaults.baseURL = "https://drf-api2023-appl-14278a611b47.gitpod.io/";
axios.defaults.headers.post["Content-Type"] = "multipart/form-data";
axios.defaults.withCredentials = true;

export const axiosReq = axios.create();
export const axiosRes = axios.create();