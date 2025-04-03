import axios from "axios";

const API_URL = "http://127.0.0.1:8000/api";

export const getSchedule = async () => {
    const response = await axios.get(`${API_URL}/schedule`);
    return response.data;
};

export const getNextRace = async () => {
    const response = await axios.get(`${API_URL}/schedule/next`);
    return response.data;
};
