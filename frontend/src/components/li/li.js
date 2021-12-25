import React from "react";


/*
 * Description: li HTML element to be used with AdminLTE
 * Props:
 *  - content: HTML element or component to be show on the list
 */

export const Li = ({ content }) => {
    const generate_random_key = () => {
        return Math.random().toString(36).replace(/[^a-z]+/g, '');
    }

    return (
        <li key={generate_random_key()} className="nav-item">
            {content}
        </li>
    )
}

