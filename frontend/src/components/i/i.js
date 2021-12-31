import React from "react";


/*
 * Description: i HTML element to work with AdminLTE
 * Props:
 *  - css_class: admin css class you want to use
 *  - content: HTML element or component to be shown
 */

export const I = ({ css_class, content }) => {
    return (
        <i className={css_class}>
            {content}
        </i>
    )
}

