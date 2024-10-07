# Usar una imagen base de nginx
FROM nginx:alpine

# Copiar el archivo HTML al contenedor de nginx
COPY index.html /usr/share/nginx/html/index.html

# Copiar la configuración personalizada de nginx al contenedor
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Exponer el puerto 8555
EXPOSE 8555

# Iniciar nginx con la nueva configuración
CMD ["nginx", "-g", "daemon off;"]