import React, { useEffect, useState } from "react";

const UsersContext = React.createContext({
    users: [], fetchUsers: () => {}
});

export default function Users() {
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
            {users.map((user) => (
                <p>{user.login}</p>
            ))}
        </UsersContext.Provider>
    );
}

