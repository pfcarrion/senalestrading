import React from 'react';
import Navbar from './Navbar'; // Importa el componente de navegación
import Footer from './Footer'; // Importa el componente del pie de página
import './Layout.css'; // Importa los estilos CSS

function Layout({ children }) {
  return (
    <div className="layout">
      <Navbar /> {/* Barra de navegación */}
      <main className="content">
        {children} {/* Contenido dinámico de cada página */}
      </main>
      <Footer /> {/* Pie de página */}
    </div>
  );
}

export default Layout;
