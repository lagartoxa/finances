import React from "react";


/*
 * Description: a HTML element to be used with AdminLTE
 * Props:
 *  - type: type of the a element
 *      - navigation: navigation link
 *      - brand: brand link
 *  - href: link to be redirected
 *  - dataWidget: bootstrap widget to be used [OPTIONAL]
 *  - role: bootstrap role for this element [OPTIONAL]
 *  - content: HTML element or component to be show on the list
 */

export const A = ({ type, href, dataWidget, role, content }) => {
    const a_classes = {
        navigation: "nav-link",
        brand: "brand-link"
    }

    return (
        <a className={a_classes[type]} href={href} data-widget={dataWidget} role={role}>
            {content}
        </a>
    )
}

