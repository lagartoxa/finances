import React from "react";


/*
 * Description: Nav HTML component to use with Adminlte
 * Props:
 *  - content: HTML element or component to be shown by this component
 *  - type:
 *      - header: gives you the classes for the header CSS
 *      - sidebar: giver you the classes for the sidebar CSS
 */
export const Nav = ({ type, content }) => {
    const nav_classes = {
        header: "main-header navbar navbar-expand navbar-white navbar-light",
        sidebar: "mt-2"
    }

    return (
        <nav className={nav_classes[type]}>
            {content}
        </nav>
    );
}

