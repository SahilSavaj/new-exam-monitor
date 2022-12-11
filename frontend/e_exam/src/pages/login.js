import React, { useState } from "react";
import '../page-styles/Forms.css'
import { Link,Route  } from "react-router-dom";
import { Navigate } from 'react-router-dom';
import Webcam from "react-webcam";
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import axios from 'axios';

const Register =() => {


    const [username,setUsername]=useState('');
    const [password,setPassword]=useState('');
    const [image,setImage]=useState('');
    const [resp,setResp]=useState('');

    const handleInputChange = (e) => {
      const {id , value} = e.target;
      // console.log()
      if(id === "username"){
        setUsername(value);
      }
      if(id === "password"){
        setPassword(value);
      }

    }
    
    const videoConstraints = {
      width: 1280,
      height: 720,
      facingMode: "user"
    };
    const webcamRef = React.useRef(null);  
        
  const Response_from_back=()=>{
    return{
      __html:`<h1>{resp}</h1>`
    };
  }
  const handleSubmit  = async (e) => {
    e.preventDefault();
    let content={
        username:username,
        password:password,
        image:webcamRef.current.getScreenshot(),
      }
    console.log(content);
    const url='http://127.0.0.1:5000/login'
        await axios.post(url, content)
        .then(response => {
          console.log(response.data)
          if(response.data.statuscode === 200){
            console.log('s')
          }
          }
          )
        .catch(error => {
        console.error('There was an error!', error);
        });
    }
    
  
  return (
      <>
      <Container fluid>
        
        <div className='login-form'>
          <div className="formCenter">
            <div className="Message-container">
            {(() => {
              if (resp!=='') {
                return (
                  <div dangerouslySetInnerHTML={Response_from_back()} />
                )
            }})()}
                
              
               
            </div>
            <form className="formFields" onSubmit={(e)=>handleSubmit(e)}>
              <Row><Col>
              <Row>
                  <h1 class='login-form-heading'>Login</h1>
              </Row>      
              <div className="formField">
                <Col className="form-labels">
                <label className="formFieldLabel" htmlFor="username">
                  User Name
                </label>
                </Col>
                <Col>
                <input
                  type="text"
                  id="username"
                  className="formFieldInput"
                  placeholder="Enter your user name"
                  name="username" 
                  // value={this.state.name}
                  onChange={(e) => handleInputChange(e)}
                /></Col>
              </div>
              <div className="formField">
              <Col className="form-labels">
                <label className="formFieldLabel" htmlFor="password">
                  Password
                </label>
                </Col>
                <Col>
                <input
                  type="password"
                  id="password"
                  className="formFieldInput"
                  placeholder="Enter your password"
                  name="password"
                  // value={this.state.name}
                  onChange={(e) => handleInputChange(e)} 
                /></Col>
              </div>

              <div className="formField">
                <button className="formFieldButton">Login</button>
              </div>

              <div className="formField">
                <Link to="/login" className="formFieldLink">
                    New user?
                </Link>
              </div>
              </Col>
              <Col>
              <div className="web-cam" >
                <Webcam
                  audio={false}
                  height={300}
                  ref={webcamRef}
                  screenshotFormat="image/jpeg"
                  width={640}
                  videoConstraints={videoConstraints}
                />
                </div>
              </Col>
              </Row>
            </form>
          </div>
        </div>
     
      </Container>
    </>
    );
}
export default Register;