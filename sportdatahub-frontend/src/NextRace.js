import React, { useEffect, useState } from "react";
import { getNextRace } from "./api";

const NextRace = () => {
    const [nextRace, setNextRace] = useState(null);

    useEffect(() => {
        async function fetchData() {
            const data = await getNextRace();
            setNextRace(data);
        }
        fetchData();
    }, []);

    if (!nextRace) return <p>Загрузка...</p>;

    return (
        <div>
            <h2>🏁 Следующая гонка</h2>
            <p><strong>{nextRace.name}</strong></p>
            <p>📍 {nextRace.location}, {nextRace.country}</p>
            <p>📆 {new Date(nextRace.date).toLocaleDateString()}</p>
            <p>⏰ {nextRace.time}</p>
        </div>
    );
};

export default NextRace;

