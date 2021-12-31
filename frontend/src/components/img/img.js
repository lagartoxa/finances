import React from "react";


export const Img = ({ css_class, alt, src}) => {
    return (
        <img src={src} alt={alt} className={css_class} />
    )
}

