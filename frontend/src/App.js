/*import React, { useState } from 'react';*/
import RegistrationForm from './RegistrationForm';
import LoginForm from './LoginForm';
import LandingPage from './LandingPage'; // Importa LandingPage
import './App.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom'; // Importa BrowserRouter y Route

function App() {
  /*const [showLogin, setShowLogin] = useState(false); // Estado para controlar qué formulario mostrar*/

  return (
    <BrowserRouter>
      <div className="App"> {/* Aplica los estilos de Flexbox aquí */}
        (
          <LoginForm />
        ) : (
          <LandingPage />
        )}
        <Routes>
          <Route path="/register" element={<RegistrationForm />} /> {/* Ruta para el registro */}
          <Route path="/login" element={<LoginForm />} /> {/* Ruta para el login */}
          <Route path="/" element={<LandingPage />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
