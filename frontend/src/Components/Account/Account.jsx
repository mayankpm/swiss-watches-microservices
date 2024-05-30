import React from 'react';
import Navbar from '../Navbar/Navbar';
import Footer from '../Footer/Footer';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import './Account.css';

export default function Account() {
    const navigate = useNavigate();
    
    const handleLogoutButton = async () => {
        try{
            axios.post('http://127.0.0.1:8000/auth/logout')
            console.log("User is logged out")

            setTimeout(() => {
                navigate('/');
            }, 2000);

        } catch(error) {
            console.error("Failed to logout:", error);
        }
    }

    return (
        <>
            <Navbar navPosition={{position: 'relative'}} navTextStyle={{color: 'white'}} navBGColor='white' navIcon={{background: 'white'}} navCartIcon='public\cart.svg' navSearchIcon='search.svg'/>
            <div>Account</div>
            <button onClick={handleLogoutButton}>Logout</button>
            <Footer/>
        </>
    )
}
