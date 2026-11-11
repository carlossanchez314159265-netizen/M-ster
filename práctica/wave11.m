% =========================================================
% RUIDO BLANCO - ENSAYO #11
% Requisito: tener cargadas t (s) y sup (m) de wave_11.mat
% Ejecutar el script ENTERO con el botón Run (F5)
% =========================================================

clearvars -except t sup
close all

% Si t y sup no están cargadas, las carga del archivo
if ~exist('t','var') || ~exist('sup','var')
    load('wave_11.mat');
end

% Comprobación: wave_11 dura unos 435 s
if abs(t(end) - 434.76) > 1
    error('t y sup no son de wave_11 (duran %.0f s). Haz load(''wave_11.mat'').', t(end));
end

t   = t(:);                  % asegurar vectores columna
sup = sup(:);
fs  = 1/(t(2) - t(1));       % frecuencia de muestreo (100 Hz)

% ---------------------------------------------------------
% 1. TRAMO DE ANÁLISIS
% ---------------------------------------------------------
tini = 45;                   % inicio del tramo (s)
tfin = 350;                  % fin del tramo (s)

idx  = (t >= tini) & (t <= tfin);
t2   = t(idx);
eta  = sup(idx) - mean(sup(idx));   % superficie libre sin la media

fprintf('Tramo analizado: %.2f s a %.2f s\n', t2(1), t2(end));

% ---------------------------------------------------------
% 2. GRÁFICAS DE LA SERIE TEMPORAL
% ---------------------------------------------------------
figure
plot(t, sup)
hold on
yl = [min(sup) max(sup)];
plot([tini tini], yl, 'r--', 'LineWidth', 1.2)
plot([tfin tfin], yl, 'r--', 'LineWidth', 1.2)
xlabel('t (s)'), ylabel('\eta (m)')
title('Ensayo #11 - serie temporal completa')
grid on, axis tight

figure
plot(t2, eta)
xlabel('t (s)'), ylabel('\eta (m)')
title('Ensayo #11 - tramo analizado')
grid on, axis tight

% ---------------------------------------------------------
% 3. CRUCES POR CERO ASCENDENTES: Hs
% ---------------------------------------------------------
c = find(eta(1:end-1) < 0 & eta(2:end) >= 0);

n = length(c) - 1;           % número de olas
H = zeros(n,1);
for i = 1:n
    tramo = eta(c(i):c(i+1));
    H(i)  = max(tramo) - min(tramo);
end

Hord = sort(H, 'descend');
N3   = round(n/3);
Hs   = mean(Hord(1:N3));     % altura significante (estadística)

% ---------------------------------------------------------
% 4. ESPECTRO (método de Welch: promedio de segmentos)
% ---------------------------------------------------------
nseg = 4096;                 % muestras por segmento (40.96 s)
paso = nseg/2;               % solape del 50 %
ventana = 0.5*(1 - cos(2*pi*(0:nseg-1)'/(nseg-1)));   % ventana de Hann
U = sum(ventana.^2);

nv = floor((length(eta) - nseg)/paso) + 1;   % número de segmentos
Sf = zeros(nseg/2 + 1, 1);
for k = 1:nv
    i0 = (k-1)*paso + 1;
    x  = eta(i0:i0+nseg-1);
    x  = x - mean(x);
    X  = fft(x .* ventana);
    p  = abs(X).^2 / (fs*U);
    p  = p(1:nseg/2+1);
    p(2:end-1) = 2*p(2:end-1);           % espectro de un solo lado
    Sf = Sf + p;
end
Sf = Sf/nv;                          % S(f) en m^2/Hz
f  = (0:nseg/2)' * fs/nseg;          % frecuencias en Hz

omega = 2*pi*f;                      % rad/s
Sw    = Sf/(2*pi);                   % S(omega) en m^2*s/rad

% ---------------------------------------------------------
% 5. MOMENTOS, Hm0 Y T02
% ---------------------------------------------------------
fmin = 0.05;  fmax = 2;              % rango de integración (Hz)
mk = (f >= fmin) & (f <= fmax);

m0 = trapz(omega(mk), Sw(mk));
m2 = trapz(omega(mk), omega(mk).^2 .* Sw(mk));

Hm0 = 4*sqrt(m0);
T02 = 2*pi*sqrt(m0/m2);              % periodo medio de cortes por cero

[~, ip] = max(Sw);
Tp_obs  = 2*pi/omega(ip);            % periodo de pico observado (referencia)

% ---------------------------------------------------------
% 6. ESPECTRO TEÓRICO JONSWAP (Hm0, Tp = 1.25*T02, gamma = 3.3)
% ---------------------------------------------------------
Tp  = 1.25*T02;
wp  = 2*pi/Tp;
gam = 3.3;
sig = 0.07*ones(size(omega));
sig(omega > wp) = 0.09;
Ag  = 1 - 0.287*log(gam);            % factor de normalización

SJ = Ag*(5/16)*Hm0^2*wp^4 .* omega.^(-5) .* exp(-1.25*(omega/wp).^(-4)) ...
     .* gam.^exp(-(omega - wp).^2 ./ (2*sig.^2*wp^2));
SJ(omega == 0) = 0;

Hm0_J = 4*sqrt(trapz(omega(mk), SJ(mk)));

% ---------------------------------------------------------
% 7. GRÁFICAS DEL ESPECTRO
% ---------------------------------------------------------
figure
plot(omega, Sw, 'LineWidth', 1.2)
xlabel('\omega (rad/s)'), ylabel('S(\omega) (m^2 s/rad)')
title('Ensayo #11 - espectro de energía')
grid on, xlim([0 2*pi*fmax])

figure
plot(omega, Sw, 'LineWidth', 1.2)
hold on
plot(omega, SJ, 'r--', 'LineWidth', 1.5)
xlabel('\omega (rad/s)'), ylabel('S(\omega) (m^2 s/rad)')
legend('Observado', 'JONSWAP (T_p = 1.25 T_{02}, \gamma = 3.3)')
title('Ensayo #11 - espectro observado frente a JONSWAP')
grid on, xlim([0 2*pi*fmax])

% ---------------------------------------------------------
% 8. RESULTADOS
% ---------------------------------------------------------
fprintf('\n--- RUIDO BLANCO ---\n')
fprintf('Número de olas:            %d\n', n)
fprintf('Segmentos promediados:     %d (df = %.4f Hz)\n', nv, fs/nseg)
fprintf('Hm0 = 4*sqrt(m0):          %.4f m\n', Hm0)
fprintf('Hs (cruces por cero):      %.4f m\n', Hs)
fprintf('Hs/Hm0:                    %.3f\n', Hs/Hm0)
fprintf('T02:                       %.3f s\n', T02)
fprintf('Tp = 1.25*T02 (JONSWAP):   %.3f s\n', Tp)
fprintf('Tp observado (pico):       %.3f s\n', Tp_obs)
fprintf('Hm0 del JONSWAP:           %.4f m\n', Hm0_J)
