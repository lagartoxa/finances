import React from "react";
import {
    A,
    I,
    Li,
    Nav,
    Ul
} from "../..";


export const Header = () => {
    const menu_icon = <I css_class="fas fa-bars" />;
    const menu_button = <A href='#' dataWidget="pushmenu" role="button" content={menu_icon} />;
    const home_button = <A href="index.html" content="Home" />;

    const buttons = [menu_button, home_button, ];

    return (
        <Nav content={ <Ul content={buttons.map((item) => <Li content={item} />)} /> } />
    );
}

