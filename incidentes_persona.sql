-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 23-04-2021 a las 02:21:13
-- Versión del servidor: 10.4.17-MariaDB
-- Versión de PHP: 7.3.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `registro_incidentes_bd`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `incidentes_persona`
--

CREATE TABLE `incidentes_persona` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `apellido_paterno` varchar(255) NOT NULL,
  `apellido_materno` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `incidentes_persona`
--

INSERT INTO `incidentes_persona` (`id`, `nombre`, `apellido_paterno`, `apellido_materno`, `email`) VALUES
(1, 'Armando', 'Berlanga', 'Mendoza', 'armando@gmail.com'),
(2, 'Fresia', 'Perez', 'Garaza', 'Fresia.perez@udem.edu'),
(3, 'Jose', 'Cardiel', 'Cardenaz', 'Carlos.lopez@udem.edu'),
(4, 'Hannia Marisol', 'Pérez', 'Garza', 'hanni'),
(5, 'Cesar', 'Botello', 'Buenaonda', 'merge.itc@gmail.com'),
(6, 'Lorenzo', 'Jaurez', 'Morales', 'MLorenzo@udem.edu'),
(7, 'Marco', 'Berlanga', 'Mendoza', 'mmendoza@hacsys.com');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `incidentes_persona`
--
ALTER TABLE `incidentes_persona`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `incidentes_persona`
--
ALTER TABLE `incidentes_persona`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
