import React, { useState } from 'react';
import { TextField, Button, Grid, Typography, Container } from '@mui/material';

function LoginForm() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setError('');
    setLoading(true);

    const userData = {
      username: username,
      password: password,
    };

    try {
      const response = await fetch('http://192.168.11.10:8000/login/', { // Ajusta la URL si es necesario
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(userData),
      });

      setLoading(false);

      if (response.ok) {
        const data = await response.json();
        // Guarda el token en el local storage o en una cookie segura
        localStorage.setItem('access_token', data.access);
        localStorage.setItem('refresh_token', data.refresh);
        console.log('Inicio de sesión exitoso');
        // Redirige al usuario a la página principal
        window.location.href = '/'; // Reemplaza '/' con la URL de tu página principal
      } else {
        const errorData = await response.json();
        if (errorData) {
          setError(JSON.stringify(errorData));
          console.error('Error en el inicio de sesión:', errorData);
        } else {
          setError(`Error en el inicio de sesión: ${response.statusText}`);
          console.error('Error en el inicio de sesión:', response.statusText);
        }
      }
    } catch (error) {
      setLoading(false);
      setError('Error de red: ' + error.message);
      console.error('Error de red:', error);
    }
  };

  return (
    <Container maxWidth="sm">
      <Typography variant="h4" align="center" gutterBottom>
        Inicio de Sesión
      </Typography>
      {error && <Typography color="error" align="center">{error}</Typography>}
      <form onSubmit={handleSubmit}>
        <Grid container spacing={2}>
          <Grid item xs={12}>
            <TextField
              label="Usuario"
              variant="outlined"
              fullWidth
              required
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
          </Grid>
          <Grid item xs={12}>
            <TextField
              label="Contraseña"
              variant="outlined"
              fullWidth
              required
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </Grid>
          <Grid item xs={12}>
            <Button variant="contained" color="primary" fullWidth type="submit" disabled={loading}>
              {loading ? 'Iniciando Sesión...' : 'Iniciar Sesión'}
            </Button>
          </Grid>
        </Grid>
      </form>
    </Container>
  );
}

export default LoginForm;
