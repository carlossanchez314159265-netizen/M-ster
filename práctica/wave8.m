% =========================================================
% OLEAJE IRREGULAR - ENSAYO #8
% Requisito: tener cargadas t (s) y sup (m) de wave_8.mat
% Ejecutar el script ENTERO con el botón Run (F5)
% =========================================================

clearvars -except t sup
close all

% Si t y sup no están cargadas, las carga del archivo
if ~exist('t','var') || ~exist('sup','var')
    load('wave_8.mat');
end

% Comprobación: wave_8 dura unos 542 s
if t(end) < 500
    error('t y sup no son de wave_8 (duran %.0f s). Haz load(''wave_8.mat'').', t(end));
end

t   = t(:);                  % asegurar vectores columna
sup = sup(:);
fs  = 1/(t(2) - t(1));       % frecuencia de muestreo (100 Hz)

% ---------------------------------------------------------
% 1. TRAMO DE ANÁLISIS
% ---------------------------------------------------------
tini = 55;                   % inicio del tramo (s)
tfin = 375;                  % fin del tramo (s)

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
title('Ensayo #8 - serie temporal completa')
grid on, axis tight

figure
plot(t2, eta)
xlabel('t (s)'), ylabel('\eta (m)')
title('Ensayo #8 - tramo analizado')
grid on, axis tight

% ---------------------------------------------------------
% 3. CRUCES POR CERO ASCENDENTES: H Y T DE CADA OLA
% ---------------------------------------------------------
c = find(eta(1:end-1) < 0 & eta(2:end) >= 0);

n  = length(c) - 1;          % número de olas
H  = zeros(n,1);             % altura de cada ola
T  = zeros(n,1);             % periodo de cada ola
tc = zeros(n,1);             % instante de inicio de cada ola

for i = 1:n
    tramo = eta(c(i):c(i+1));
    H(i)  = max(tramo) - min(tramo);
    T(i)  = t2(c(i+1)) - t2(c(i));
    tc(i) = t2(c(i));
end

% ---------------------------------------------------------
% 4. ESTADÍSTICOS DE ALTURA Y PERIODO
% ---------------------------------------------------------
[Hord, orden] = sort(H, 'descend');   % de mayor a menor
Tord = T(orden);                      % periodos en el mismo orden
N3   = round(n/3);                    % tercio de olas más altas

Hs   = mean(Hord(1:N3));
Hrms = sqrt(mean(H.^2));
Hmed = mean(H);
[Hmax, imax] = max(H);
t_Hmax = tc(imax);

Tmed   = mean(T);
T13    = mean(Tord(1:N3));
T_Hmax = T(imax);

eta_max = max(eta);

% ---------------------------------------------------------
% 5. DISTRIBUCIÓN DE ALTURAS Y RAYLEIGH
% ---------------------------------------------------------
Hasc = sort(H);                       % de menor a mayor
P    = (1:n)' / (n+1);                % probabilidad de no excedencia

H2_emp = interp1(P, Hasc, 0.98);      % superada solo por el 2%
H2_ray = Hrms * sqrt(-log(0.02));     % de exp(-(H/Hrms)^2) = 0.02

Hmax_Hs_ray = sqrt(log(n)/2);         % Hmax/Hs esperado (Rayleigh)

Hx = linspace(0, max(H)*1.1, 200);
F_ray = 1 - exp(-(Hx/Hrms).^2);       % distribución de Rayleigh

figure
plot(Hasc, P, 'o', 'MarkerSize', 4)
hold on
plot(Hx, F_ray, 'r', 'LineWidth', 1.5)
xlabel('H (m)'), ylabel('P(H'' \leq H)')
legend('Empírica', 'Rayleigh', 'Location', 'southeast')
title('Ensayo #8 - función de distribución de alturas de ola')
grid on

% ---------------------------------------------------------
% 6. RESULTADOS
% ---------------------------------------------------------
fprintf('\n--- ANÁLISIS ESTADÍSTICO ---\n')
fprintf('Número de olas:            %d\n', n)
fprintf('Hs:                        %.4f m\n', Hs)
fprintf('Hrms:                      %.4f m\n', Hrms)
fprintf('Hmedia:                    %.4f m\n', Hmed)
fprintf('Hmax:                      %.4f m  (t = %.2f s)\n', Hmax, t_Hmax)
fprintf('Hmax/Hs:                   %.3f\n', Hmax/Hs)
fprintf('eta_max/Hmax:              %.3f\n', eta_max/Hmax)
fprintf('Tmedio:                    %.3f s\n', Tmed)
fprintf('T1/3:                      %.3f s\n', T13)
fprintf('T de la ola máxima:        %.3f s\n', T_Hmax)
fprintf('\n--- DISTRIBUCIÓN DE ALTURAS ---\n')
fprintf('H2%% empírica:              %.4f m\n', H2_emp)
fprintf('H2%% Rayleigh:              %.4f m\n', H2_ray)
fprintf('Hmax/Hs Rayleigh (N=%d):   %.3f\n', n, Hmax_Hs_ray)
fprintf('\n--- COMPROBACIÓN RAYLEIGH ---\n')
fprintf('Hs/Hrms:   %.3f  (Rayleigh: 1.416)\n', Hs/Hrms)
fprintf('Hmed/Hrms: %.3f  (Rayleigh: 0.886)\n', Hmed/Hrms)

% ---------------------------------------------------------
% 7. ESPECTRO (método de Welch: promedio de segmentos)
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
% 8. MOMENTOS Y PARÁMETROS ESPECTRALES
% ---------------------------------------------------------
fmin = 0.05;  fmax = 2;              % rango de integración (Hz)
mk = (f >= fmin) & (f <= fmax);

m = zeros(5,1);                      % m(1)=m0, m(2)=m1, ..., m(5)=m4
for n = 0:4
    m(n+1) = trapz(omega(mk), omega(mk).^n .* Sw(mk));
end
m0 = m(1); m1 = m(2); m2 = m(3); m4 = m(5);

rho = 1000;  g = 9.81;               % agua dulce del canal
Hm0 = 4*sqrt(m0);
E   = rho*g*m0;                      % J/m^2

[~, ip] = max(Sw);
wp = omega(ip);
Tp = 2*pi/wp;

T01   = 2*pi*m0/m1;
Tz    = 2*pi*sqrt(m0/m2);
T24   = 2*pi*sqrt(m2/m4);
epsil = sqrt(1 - m2^2/(m0*m4));

% ---------------------------------------------------------
% 9. ESPECTRO TEÓRICO JONSWAP (Hm0, Tp, gamma = 3.3)
% ---------------------------------------------------------
gam = 3.3;
sig = 0.07*ones(size(omega));
sig(omega > wp) = 0.09;
Ag  = 1 - 0.287*log(gam);            % factor de normalización

SJ = Ag*(5/16)*Hm0^2*wp^4 .* omega.^(-5) .* exp(-1.25*(omega/wp).^(-4)) ...
     .* gam.^exp(-(omega - wp).^2 ./ (2*sig.^2*wp^2));
SJ(omega == 0) = 0;

Hm0_J = 4*sqrt(trapz(omega(mk), SJ(mk)));

% ---------------------------------------------------------
% 10. GRÁFICAS DEL ESPECTRO
% ---------------------------------------------------------
figure
plot(omega, Sw, 'LineWidth', 1.2)
xlabel('\omega (rad/s)'), ylabel('S(\omega) (m^2 s/rad)')
title('Ensayo #8 - espectro de energía')
grid on, xlim([0 2*pi*fmax])

figure
plot(omega, Sw, 'LineWidth', 1.2)
hold on
plot(omega, SJ, 'r--', 'LineWidth', 1.5)
xlabel('\omega (rad/s)'), ylabel('S(\omega) (m^2 s/rad)')
legend('Observado', 'JONSWAP (\gamma = 3.3)')
title('Ensayo #8 - espectro observado frente a JONSWAP')
grid on, xlim([0 2*pi*fmax])

% ---------------------------------------------------------
% 11. RESULTADOS ESPECTRALES
% ---------------------------------------------------------
fprintf('\n--- ANÁLISIS ESPECTRAL ---\n')
fprintf('Segmentos promediados:     %d (df = %.4f Hz)\n', nv, fs/nseg)
fprintf('m0:                        %.4e m^2\n', m0)
fprintf('Hm0:                       %.4f m\n', Hm0)
fprintf('E = rho*g*m0:              %.2f J/m^2\n', E)
fprintf('Tp:                        %.3f s\n', Tp)
fprintf('T01:                       %.3f s\n', T01)
fprintf('Tz:                        %.3f s\n', Tz)
fprintf('T24:                       %.3f s\n', T24)
fprintf('epsilon:                   %.3f\n', epsil)
fprintf('Hm0 del JONSWAP:           %.4f m\n', Hm0_J)
