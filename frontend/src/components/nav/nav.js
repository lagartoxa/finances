import React from "react";


/*
 * Description: Nav HTML component to use with Adminlte
 * Props:
 *  - content: HTML element or component to be shown by this component
 */
export const Nav = ({ content }) => {
    return (
        <nav className="main-header navbar navbar-expand navbar-white navbar-light">
            {content}
        </nav>
    );
}

