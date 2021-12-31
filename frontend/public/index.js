import React from "react";
import ReactDOM from "react-dom";
import { Header, Sidebar } from "../src";


const App = () => {
    return (
        <div>
            <Header />
            <Sidebar />
        </div>
    )
}

ReactDOM.render(<App />, document.getElementById("header"));

