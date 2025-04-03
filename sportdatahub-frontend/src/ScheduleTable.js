import React, { useEffect, useState } from "react";
import { getSchedule } from "./api";

const ScheduleTable = () => {
    const [schedule, setSchedule] = useState([]);

    useEffect(() => {
        async function fetchData() {
            const data = await getSchedule();
            setSchedule(data);
        }
        fetchData();
    }, []);

    return (
        <div>
            <h2>📅 Расписание гонок</h2>
            <table border="1">
                <thead>
                    <tr>
                        <th>Этап</th>
                        <th>Название</th>
                        <th>Страна</th>
                        <th>Дата</th>
                        <th>Время</th>
                    </tr>
                </thead>
                <tbody>
                    {schedule.map((race) => (
                        <tr key={race.round}>
                            <td>{race.round}</td>
                            <td>{race.name}</td>
                            <td>{race.country}</td>
                            <td>{new Date(race.date).toLocaleDateString()}</td>
                            <td>{race.time}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default ScheduleTable;

