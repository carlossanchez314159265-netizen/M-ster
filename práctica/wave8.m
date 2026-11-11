%% Oleaje irregular - Ensayo #8
clear; close all; clc;

%% 1. Carga de datos
load('wave_8.mat');          % variables: t (s) y sup (m)
fs = 1/(t(2) - t(1));        % frecuencia de muestreo (100 Hz)

%% 2. Tramo de análisis
t_ini = 55;                  % s
t_fin = 375;                 % s

idx  = (t >= t_ini) & (t <= t_fin);
t2   = t(idx);
sup2 = sup(idx);
eta  = sup2 - mean(sup2);    % superficie libre respecto al nivel medio

fprintf('Tramo: %.2f s a %.2f s (%d muestras)\n', t2(1), t2(end), length(t2));

%% 3. Gráficas de la serie temporal
figure;
plot(t, sup); hold on;
xline(t_ini, 'r--', 'LineWidth', 1.2);
xline(t_fin, 'r--', 'LineWidth', 1.2);
xlabel('t (s)'); ylabel('\eta (m)');
title('Ensayo #8 - serie temporal completa');
grid on; axis tight;

figure;
plot(t2, eta);
xlabel('t (s)'); ylabel('\eta (m)');
title(sprintf('Ensayo #8 - tramo analizado (%g-%g s)', t_ini, t_fin));
grid on; axis tight;

%% 4. Cruces por cero ascendentes
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

fprintf('Número de olas: %d\n', n);

%% 5. Análisis estadístico
% Completa cada línea siguiendo las indicaciones.

% Ordenar las olas de mayor a menor altura (los periodos en el mismo orden)
[Hord, orden] = sort(H, 'descend');
Tord = T(orden);
N3   = round(n/3);           % número de olas del tercio más alto

% Hs    = ...   % media de las N3 primeras de Hord
% Hrms  = ...   % sqrt(mean(H.^2))
% Hmed  = ...   % media de H
% [Hmax, imax] = max(H);
% t_Hmax = ...  % instante de la ola máxima (usa tc)

% Tmed  = ...   % media de T
% T13   = ...   % media de las N3 primeras de Tord
% T_Hmax = ...  % periodo de la ola máxima (usa imax)

% Hmax/Hs   = ...
% eta_max   = max(eta);
% eta_max/Hmax = ...

%% 6. Distribución de alturas y Rayleigh
% Hasc = sort(H);                  % de menor a mayor
% P    = (1:n)'/(n+1);             % probabilidad de no excedencia
% figure; plot(Hasc, P, 'o'); ...  % función de distribución empírica

% H2_emp = ...   % altura superada solo por el 2% (P = 0.98)
% H2_ray = ...   % despejar de exp(-(H/Hrms)^2) = 0.02
% Hmax_Hs_ray = sqrt(log(n)/2);    % lo esperado según Rayleigh
