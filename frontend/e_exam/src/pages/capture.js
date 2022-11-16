import React,{useState,useEffect} from 'react';
import Webcam from "react-webcam";
import '../page-styles/Forms.css'
import Container from 'react-bootstrap/Container';


const Capture = () => {
    const [image,setImage]=useState('');
    const videoConstraints = {
        width: 1280,
        height: 720,
        facingMode: "user"
      };

    const webcamRef = React.useRef(null);
    const capture = React.useCallback(
        () => {
        const imageSrc = webcamRef.current.getScreenshot();
        setImage(imageSrc);   
        }   
        ,[webcamRef]
      
        ); 
    const chal=(e)=>{
      e.preventDefault();
      capture();
    } 
    return (
      <>
      <Container fluid>
      <div className='login-form'>
      <div className="formCenter">
    
      <form >
      <div className="formField" >
        <Webcam
          audio={false}
          height={360}
          ref={webcamRef}
          screenshotFormat="image/jpeg"
          width={640}
          videoConstraints={videoConstraints}
        />
        </div>
        <div className="formField">
            <button className="formFieldButton" onClick={chal}>Capture</button>
            {/* <button className="formFieldButton" onClick={()=> {capture();}}>Capture</button> */}

        </div>
        </form>

        </div>
        </div>
        </Container>
      </>
    );
  };

export default Capture;