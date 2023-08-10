import pygame
import math
import numpy as np
from numba import jit, float64, int32, vectorize

# Inicializar pygame
pygame.init()

# Definir colores
c_BACK = (200, 200, 200)

# Establecer dimensiones de la ventana
ANCHO, ALTO = 800, 600
Zx, Zy = 6, 40 
X0, Y0 = 50, ALTO/2

# Crear ventana y reloj
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Simulación de Cuerda")
reloj = pygame.time.Clock()

@jit('Tuple((float64[:,:], float64[:,:]))(int64, float64[:,:], float64[:,:], float64, float64, float64, float64, float64)', nopython=True)
def integrate(N, X, V, dt, k, mu, m, deq):
    for n in range(1000):
        # === distances === 
        dX = X[1:,:] - X[:-1,:]
        d = (dX[:,0]**2 + dX[:,1]**2)**0.5
        fdX = dX/d.reshape(-1, 1)

        # === forces === 
        Total_Force = np.zeros((N,2)) 

        Fe = (d.reshape(-1, 1)-deq)*k*fdX 
        Total_Force[:-1,:] += Fe
        Total_Force[1:,:] -= Fe

        Fg = np.ones(N)*m 
        Total_Force[:,1] += Fg

        Ff = V*mu 
        Total_Force -= Ff

        # === verlet 1st integration === 
        V += Total_Force/10*dt/2
        X[1:-1,:] += V[1:-1,:]*dt

        # === distances === 
        dX = X[1:,:] - X[:-1,:]
        d = (dX[:,0]**2 + dX[:,1]**2)**0.5
        fdX = dX/d.reshape(-1, 1)

        # === forces === 
        Total_Force = np.zeros((N,2)) 

        Fe = (d.reshape(-1, 1)-deq)*k*fdX 
        Total_Force[:-1,:] += Fe
        Total_Force[1:,:] -= Fe

        Fg = np.ones(N)*m 
        Total_Force[:,1] += Fg

        Ff = V*mu
        Total_Force -= Ff

        # === verlet 2nd integration === 
        V += Total_Force/10*dt/2

    return X, V

# Definir clase para un segmento de la cuerda
class String:
    def __init__(self, N, X=None):
        self.color = (150, 50, 50)
        self.N = N #numero de segmentos
        self.Ns = self.N-1
        
        self.dt = 0.09
        self.dt2 = self.dt/2
        
        self.k = 1
        self.d_eq = 1
        self.m = 0.00001
        self.mu = 0.001

        self.X = X if not X is None else np.array( [np.arange(self.N, dtype=np.float64), np.sin(np.arange(self.N, dtype=np.float64)/10) * 0.5] , dtype=np.float64).T
        
        self.V = np.zeros_like(self.X, dtype=np.float64) 
        self.a = np.zeros_like(self.X, dtype=np.float64) 

        self.F = np.zeros_like(self.X, dtype=np.float64) 

# Crear cuerda
string = String(N=100)

# Bucle principal
RUN = True
mover_cuerda = False
while RUN:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            RUN = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            mover_cuerda = True
        if evento.type == pygame.MOUSEBUTTONUP:
            mover_cuerda = False

    ventana.fill(c_BACK)

    # Actualizar 
    string.X, string.V = integrate(string.N, string.X, string.V, string.dt, string.k, string.mu, string.m, string.d_eq)

    # dibujar segmentos de la cuerda
    for Ni in range(1, string.N):
        pygame.draw.line(ventana, string.color, ( string.X[Ni-1,0]*Zx+X0, string.X[Ni-1,1]*Zy+Y0 ), (string.X[Ni,0]*Zx+X0, string.X[Ni,1]*Zy+Y0 ), 2)

    # Si el usuario está moviendo la cuerda
    if mover_cuerda:
        mx, my = pygame.mouse.get_pos()
        string.X[1:-1, 1] -= np.e**( -(int((mx-X0)/Zx % string.N) - np.arange(string.N-2))**2/50 ) 

    pygame.display.flip()
    reloj.tick(100)

pygame.quit()

