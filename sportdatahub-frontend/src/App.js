import React from "react";
import ScheduleTable from "./ScheduleTable";
import NextRace from "./NextRace";

function App() {
    return (
        <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
            <h1>🏎 SportDataHub</h1>
            <NextRace />
            <ScheduleTable />
        </div>
    );
}

export default App;

