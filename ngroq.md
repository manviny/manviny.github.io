¡Entendido! Si buscas **soluciones gratuitas y de código abierto** para exponer servicios locales y saltar firewalls, aquí tienes una lista de herramientas **open source** que puedes usar:

---

### 1. **frp (Fast Reverse Proxy)**  
   - **Descripción**: frp es una herramienta de código abierto que permite exponer servicios locales a través de un servidor intermedio (puedes usar uno propio o uno público).
   - **Características**:
     - Soporta TCP, UDP, HTTP y HTTPS.
     - Altamente configurable.
     - Puedes autohospedar el servidor.
   - **Repositorio**: [https://github.com/fatedier/frp](https://github.com/fatedier/frp)

---

### 2. **bore**  
   - **Descripción**: bore es una alternativa moderna y sencilla a Ngrok, escrita en Rust. Es ligera y fácil de usar.
   - **Características**:
     - Soporta TCP.
     - No requiere configuración compleja.
     - Puedes autohospedar el servidor.
   - **Repositorio**: [https://github.com/ekzhang/bore](https://github.com/ekzhang/bore)

---

### 3. **inlets**  
   - **Descripción**: inlets es una herramienta de tunneling de código abierto que permite exponer servicios locales detrás de firewalls o NAT.
   - **Características**:
     - Soporta HTTP y TCP.
     - Puedes usar un servidor propio o uno público.
     - Ideal para Kubernetes y entornos cloud.
   - **Repositorio**: [https://github.com/inlets/inlets](https://github.com/inlets/inlets)

---

### 4. **chisel**  
   - **Descripción**: chisel es una herramienta de tunneling que funciona sobre HTTP/HTTPS y SSH. Es liviana y fácil de configurar.
   - **Características**:
     - Soporta TCP y UDP.
     - Puedes usarlo como cliente o servidor.
     - Ideal para saltar firewalls restrictivos.
   - **Repositorio**: [https://github.com/jpillora/chisel](https://github.com/jpillora/chisel)

---

### 5. **sish**  
   - **Descripción**: sish es un servidor de tunneling que usa SSH para exponer servicios locales. Es similar a Serveo, pero puedes autohospedarlo.
   - **Características**:
     - Soporta HTTP, HTTPS y TCP.
     - URLs personalizables.
     - Fácil de configurar.
   - **Repositorio**: [https://github.com/antoniomika/sish](https://github.com/antoniomika/sish)

---

### 6. **PageKite (Open Source)**  
   - **Descripción**: PageKite tiene una versión de código abierto que puedes autohospedar para exponer servicios locales.
   - **Características**:
     - Soporta HTTP y HTTPS.
     - Ideal para servidores web.
     - Fácil de configurar.
   - **Repositorio**: [https://github.com/pagekite/PyPagekite](https://github.com/pagekite/PyPagekite)

---

### 7. **sshuttle**  
   - **Descripción**: sshuttle es una herramienta de tunneling que usa SSH para redirigir tráfico de red. No requiere configuración en el servidor remoto.
   - **Características**:
     - Soporta TCP y UDP.
     - Fácil de usar.
     - Ideal para saltar firewalls.
   - **Repositorio**: [https://github.com/sshuttle/sshuttle](https://github.com/sshuttle/sshuttle)

---

### 8. **localhost.run (Open Source)**  
   - **Descripción**: localhost.run es una herramienta que permite exponer servicios locales usando SSH. Puedes autohospedar el servidor.
   - **Características**:
     - Soporta HTTP y HTTPS.
     - No requiere instalación adicional.
   - **Repositorio**: [https://github.com/localhost-run/localhost.run](https://github.com/localhost-run/localhost.run)

---

### 9. **WireGuard**  
   - **Descripción**: WireGuard es una VPN moderna y de código abierto que puedes usar para crear túneles seguros y acceder a servicios locales.
   - **Características**:
     - Ligero y rápido.
     - Soporta TCP y UDP.
     - Ideal para saltar firewalls de forma segura.
   - **Repositorio**: [https://www.wireguard.com](https://www.wireguard.com)

---

### 10. **Tailscale (Open Source Core)**  
   - **Descripción**: Tailscale es una VPN basada en WireGuard que facilita la creación de redes privadas. Tiene un núcleo de código abierto.
   - **Características**:
     - Fácil de configurar.
     - Soporta múltiples dispositivos.
     - Ideal para acceder a servicios locales de forma segura.
   - **Repositorio**: [https://github.com/tailscale/tailscale](https://github.com/tailscale/tailscale)

---

### Recomendaciones:
- Si buscas **simplicidad**, prueba **bore** o **chisel**.
- Si necesitas **autohospedar** un servidor, **frp** o **sish** son excelentes opciones.
- Para **seguridad avanzada**, considera **WireGuard** o **Tailscale**.

Todas estas herramientas son gratuitas, de código abierto y te permiten saltar firewalls de manera efectiva. ¡Elige la que mejor se adapte a tus necesidades! 🚀