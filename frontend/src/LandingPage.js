import React from 'react';
import Layout from './components/Layout';
import { Link } from 'react-router-dom'; // Si usas React Router
import './LandingPage.css'; // Importa los estilos CSS
import trading1 from './img/trading1.jpg'; // Importa las imágenes
import trading2 from './img/trading2.jpg';
import trading3 from './img/trading3.jpg';

function LandingPage() {
  return (
    <div className="home-page">
      <div className="hero">
        <h1>Maximiza tus Ganancias con Nuestras Señales de Trading</h1>
        <p>Señales de forex y opciones binarias de alta precisión, compatibles con cualquier broker.</p>
        <Link to="/suscribirse" className="btn btn-primary">Comienza Ahora</Link> {/* Reemplaza con tu ruta */}
      </div>

      <section className="about">
        <div className="about-section">
          <img src={trading1} alt="Gráficos de trading" className="zoomable-image" />
          <h2>Maximiza tus Ganancias con Señales de 88% de Precisión</h2>
          <p>Recibe señales con una precisión promedio del 88%, basadas en análisis de [menciona tu metodología] y probadas por nuestros expertos. Mira cómo puedes transformar tus operaciones con nuestras alertas confiables.</p>
          <Link to="/suscribirse" className="btn btn-secondary">Descubre Cómo Funciona</Link> {/* Reemplaza con tu ruta */}
        </div>

        <div className="about-section">
          <img src={trading2} alt="Análisis del Mercado" className="zoomable-image" />
          <h2>Estrategias Probadas por Expertos para un Éxito Garantizado</h2>
          <p>Nuestras estrategias están respaldadas por más de [número] años de experiencia en el mercado y un equipo de analistas profesionales. Con una tasa de pérdida de solo un 2%, te brindamos la confianza que necesitas para alcanzar tus metas.</p>
          <Link to="/suscribirse" className="btn btn-secondary">Ver Resultados</Link> {/* Reemplaza con tu ruta */}
        </div>

        <div className="about-section">
          <img src={trading3} alt="Trading en tiempo real" className="zoomable-image" />
          <h2>Recibe Alertas Instantáneas para Operaciones Rentables</h2>
          <p>Recibe señales instantáneas al momento, diseñadas para maximizar tus ganancias en cada operación. No pierdas ni una oportunidad.</p>
          <Link to="/suscribirse" className="btn btn-secondary">Obtén una Prueba Gratuita</Link> {/* Reemplaza con tu ruta */}
        </div>
      </section>
    </div>
  );
}

export default LandingPage;
