import React, { useEffect, useState } from "react";

const UsersContext = React.createContext({
    users: [], fetchUsers: () => {}
});

const AddUser = () => {
    const [item, setItem] = React.useState('');
    const {users, fetchUsers} = React.useContext(UsersContext);

    const handleInput = event => {
        setItem(event.target.value);
    };

    const handleSubmit = (event) => {
        const new_user = {
            "id": users.length + 1,
            "login": item,
        };

        console.log("NEW USER ", new_user, " ITEM: ", item);

        fetch("http://localhost:8000/user", {
            method: "POST",
            headers: {"Content-Type": "application/json", },
            body: JSON.stringify(new_user),
        }).then(fetchUsers);
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input
                    onChange={handleInput}
                    placeholder="Type new login here"
                />
            </form>
        </div>
    );
}

export const Users = () => {
    const [users, setUsers] = useState([]);
    const fetchUsers = async () => {
        const response = await fetch("http://localhost:8000/users");
        const users = await response.json();
        setUsers(users.users);
    };

    useEffect(() => {
        fetchUsers()
    }, []);

    return (
        <UsersContext.Provider value={{users, fetchUsers}}>
            <AddUser />
            {users.map((user) => (
                <p>{user.login}</p>
            ))}
        </UsersContext.Provider>
    );
}

