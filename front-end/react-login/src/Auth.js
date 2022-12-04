
import React from "react"
import axios from "axios";
import {useState} from 'react';
const baseURL = "http://localhost:8000/user/login/";
export default function (props) {
    const [post, setPost] = React.useState(null);
    const [IdentificicationNumber, setIdentificicationNumber] = useState('');
    const [password, setPassword] = useState('');

    const handleChangeIdentificicationNumber = event => {
        setIdentificicationNumber(event.target.value);

        console.log('value is:', event.target.value);
    };

    const handleChangePassword = event => {
        setPassword(event.target.value);

        console.log('value is:', event.target.value);
    };
    
    const handleClick = (e) => {
        e.preventDefault();      

        axios.post(baseURL, {
            "IdentificicationNumber":IdentificicationNumber,
            "password":password,
          })
          .then(function (response) {
            console.log(response.data);
          })
          .catch(function (error) {
            console.log(error);
          });
      }

    React.useEffect(() => {
     
    }, []);


  
  return (
    <div className="Auth-form-container">
      <form className="Auth-form">
        <div className="Auth-form-content">
          <h3 className="Auth-form-title">Sign In</h3>
          <div className="form-group mt-3">
            <label>Identificication Number address</label>
            <input
              type="IdentificicationNumber"
              onChange={handleChangeIdentificicationNumber}
              value={IdentificicationNumber}
              className="form-control mt-1"
              placeholder="Enter Identificication Number"
            />
          </div>
          <div className="form-group mt-3">
            <label>Password</label>
            <input
              type="password"
              
              onChange={handleChangePassword}
              value={password}
              className="form-control mt-1"
              placeholder="Enter password"
            />
          </div>
          <div className="d-grid gap-2 mt-3">

            <button type="submit" className="btn btn-primary" onClick={handleClick}>
              Login
            </button>
            
          </div>
          <p className="forgot-password text-right mt-2">
            Forgot <a href="#">password?</a>
          </p>
        </div>
      </form>
    </div>
  )
}