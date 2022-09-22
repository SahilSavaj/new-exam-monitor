import React,{useState,useEffect} from 'react';
import Webcam from "react-webcam";
import '../page-styles/Forms.css'
import Container from 'react-bootstrap/Container';
import b64toFile from 'b64-to-file';


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
        // setImage(imageSrc); 
        const convertedFile =b64toFile(imageSrc,'image-test');
        const url='http://172.17.0.2:5000/capture?';
        
        const params='image='.concat(imageSrc);
        // fetch(url.concat(params),{
        //   method:'POST',
        // })
        // .then(response => response.json())
        // .then(response => console.log(response))
        // .catch(error => console.log(error))
        },
        
        [webcamRef]
        
    );
  
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
            <button className="formFieldButton" onClick={(e)=>{e.preventDefault();capture();}}>Capture</button>
        </div>
        </form>

        </div>
        </div>
        </Container>
      </>
    );
  };

export default Capture;