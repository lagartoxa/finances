import React from "react";


/*
 * Description: ul HTML element to use with AdminLTE
 * Props:
 *  - content: list to be shown inside the ul
 */

export const Ul = ({ content }) => {
    return (
        <ul className="navbar-nav">
            {content}
        </ul>
    )
}

