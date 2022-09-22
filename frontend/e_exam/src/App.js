import React from 'react';
import './App.css';

import Navbar from './components/navBar';
import Home from './pages/home';
import Login from './pages/login';
import Register from './pages/register';
import Contact from './pages/contact';
import Capture from './pages/capture'
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';

function App() {
  return (
    <>
    
      <div className='mask'>
      
      <Router>
        <Navbar/>
        <Routes>
            <Route exact path='/' element={<Home />} />
            <Route path='/contact' element={<Contact/>} />
            <Route path='/register' element={<Register/>} />
            <Route path='/login' element={<Login/>} />
            <Route path='/capture' element={<Capture/>} />
        </Routes>
    </Router>
    </div>
    </>
    
  );
}

export default App;
