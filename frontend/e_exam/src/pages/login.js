import React, { Component } from 'react';
import '../page-styles/Forms.css'
import { Link } from "react-router-dom";

import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

class Login extends Component {
  constructor() {
    super();

    this.state = {
      username:"",
      password: "",
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    let target = event.target;
    let value = target.type === "checkbox" ? target.checked : target.value;
    let name = target.name;

    this.setState({
      [name]: value
    });
  }

  handleSubmit(e) {
    e.preventDefault();

    console.log("The form was submitted with the following data:");
    console.log(this.state);
  }  
  render(){
  return (
      <>
      <Container fluid>
        
        <div className='login-form'>
          <div className="formCenter">
            <form className="formFields" onSubmit={this.handleSubmit}>
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
                  id="text"
                  className="formFieldInput"
                  placeholder="Enter your user name"
                  name="username" 
                  value={this.state.name}
                  onChange={this.handleChange}
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
                  value={this.state.name}
                  onChange={this.handleChange} 
                /></Col>
              </div>

              <div className="formField">
                <button className="formFieldButton">Login</button>
              </div>

              <div className="formField">
                <Link to="/login" className="formFieldLink">
                    New Registration?
                </Link>
              </div>
              
            </form>
          </div>
        </div>
     
      </Container>
    </>
    );
  }
}
  
export default Login;