import React from "react";


/*
 * Description: ul HTML element to use with AdminLTE
 * Props:
 *  - content: list to be shown inside the ul
 *  - css_class: AdminLTE css class to be used
 */

export const Ul = ({ css_class, content }) => {
    return (
        <ul className={css_class}>
            {content}
        </ul>
    )
}

