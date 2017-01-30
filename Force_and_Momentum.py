#f = ma
def find_force(m, a):
    return m * a

#normal force = mg + m(ay)
def normal_force(m, ay):
    return m * 9.81 + m * ay

#kin. friction force = (coeff. kin. frict.)* (Normal Force)
def kin_friction(nf, kf):
    return nf * kf

#static firctional force = (coeff. static frict) * (normal force)
def stat_friction(nf, sf):
    return nf * sf

#drag force = 1/2CpAv^2, p = air density, A is area, C = drag coefficient
def drag_force(C, p, A, v):
    return (C * p * A * v * v)/2

#terminal speed = sqrt(2fg/CpA)
def terminal_speed(C, p, a, A):
    return sqrt((2 * f * g) / (C * p * A))

#centripetal force = mv^2/R
def centripetal_force(m, v, R):
    return m * v * v / R

#kinetic energy = 1/2mv^2
def kin_energy(m, v):
    return (m * v * v) / 2

#work = force * distance
def work_fun(f, d):
    return f * d

#hooke's law: fx = -kx, w = 1/2kx^2i - 1/2kx^2f
def hooke(k, x):
    return -1 * k * x

def hooke_work(k, xi, xf):
    return (k * xi * xi / 2) - (k * xf * xf / 2)

#center of mass (two): (m1x1 + m2x2)/M
def center_of_mass():
    M = 0
    top = 0
    num = int(raw_input("How many particles?"))
    for i in range(0, num):
        mass[i] = int(raw_input("Please enter particle ", i + 1))
        position[i] = int(raw_input("Please enter position of particle ", i + 1))
        M += mass[i]
    for i in range(0, num):
        top += mass[i] * position[i]
    return top / M

#density = mass / volume
def density(m, v):
    return m / v

#linear momentum = mv
def lin_momentum(m, v):
    lin_momentum = m, v

#f = dp/dt

#impulse = change in momentum = F*(change in time)
def impulse(F, tf, ti):
    return F * (tf - ti)

#cons. of linear mom: p1 + p2 = p1f + p2f

#inelastic collision velocity = (m1/(m1+m2))(v1i)


#velocity of center of mass = (p1 + p2)/(m1+m2)
def velocity_center_of_mass():
    top = 0
    M = 0
    num = int(raw_input("How many particles?"))
    for i in range(0, num):
        momentum[i] = int(raw_input("Please enter particle ", i + 1))
        mass[i] = int(raw_input("Please enter position of particle ", i + 1))
    for i in range(0, num):
        top += momentum[i]
        M += mass[i]
    return top / M

#thrust = Ma = (Rate of fuel consumption)(velocity of rocket rel)(acceleration)
