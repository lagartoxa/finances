import React from "react";


/*
 * Description: a HTML element to be used with AdminLTE
 * Props:
 *  - href: link to be redirected
 *  - dataWidget: bootstrap widget to be used [OPTIONAL]
 *  - role: bootstrap role for this element [OPTIONAL]
 *  - content: HTML element or component to be show on the list
 */

export const A = ({ href, dataWidget, role, content }) => {
    return (
        <a className="nav-link" href={href} data-widget={dataWidget} role={role}>
            {content}
        </a>
    )
}

