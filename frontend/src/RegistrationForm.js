import React, { useState } from 'react';
import { TextField, Button, Grid, Typography, Container } from '@mui/material';

function RegistrationForm() {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [error, setError] = useState('');
  const [successMessage, setSuccessMessage] = useState('');
  const [loading, setLoading] = useState(false);
  const [emailError, setEmailError] = useState('');

  const validateEmail = (email) => {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    console.log('Formulario enviado'); // <-- Añade esta línea
    setError('');
    setSuccessMessage('');
    setLoading(true);
    setEmailError('');

    if (!validateEmail(email)) {
      setEmailError('Por favor, introduce un correo electrónico válido.');
      setLoading(false);
      return;
    }

    if (password !== confirmPassword) {
      setError('Las contraseñas no coinciden');
      setLoading(false);
      return;
    }

    const userData = {
      username: username,
      email: email,
      password: password,
    };
    console.log(userData); // <-- Añade esta línea

    try {
      const response = await fetch('http://192.168.11.10:8000/register/', { // Ajusta la URL si es necesario
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(userData),
      });

      setLoading(false);

      if (response.ok) {
        setSuccessMessage('¡Registro exitoso! Redirigiendo...');
        console.log('Registro exitoso');
        setTimeout(() => {
          window.location.href = '/login'; // Reemplaza '/login' con la URL de tu página de inicio de sesión
        }, 2000);
      } else {
        const errorData = await response.json();
        if (errorData) {
          setError(JSON.stringify(errorData));
          console.error('Error en el registro:', errorData);
        } else {
          setError(`Error en el registro: ${response.statusText}`);
          console.error('Error en el registro:', response.statusText);
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
        Registro de Usuario
      </Typography>
      {error && <Typography color="error" align="center">{error}</Typography>}
      {successMessage && <Typography color="success" align="center">{successMessage}</Typography>}
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
              label="Email"
              variant="outlined"
              fullWidth
              required
              //  type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              error={!!emailError}
              helperText={emailError}
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
            <TextField
              label="Confirmar Contraseña"
              variant="outlined"
              fullWidth
              required
              type="password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
            />
          </Grid>
          <Grid item xs={12}>
            <Button variant="contained" color="primary" fullWidth type="submit" disabled={loading}>
              {loading ? 'Registrando...' : 'Registrarse'}
            </Button>
          </Grid>
        </Grid>
      </form>
    </Container>
  );
}

export default RegistrationForm;
