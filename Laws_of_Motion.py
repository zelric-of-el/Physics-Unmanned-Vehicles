#v = displacement/time, instant. v = dr/dt,
velocity(xi, xf, ti, tf){
    return (xf - xi)/(tf - ti)
}

#a = dv/dt
acceleration(vi, vf, ti, tf){
    return (vf - vi)/(tf - ti)
}

#trajectory = tan(initial theta)x - gx^2/2(initial velocity * cos(initial theta))^2
trajectory_point(x, theta, velocity){
    return tan(theta) * x - ((9.81 * (x * x)) / (2 * pow(velocity * cos(theta), 2))
}

#horizontal range of trajectory = ((initial velocity)^2/g)*2*sin(initial theta)
trajectory_distance_x(theta, velocity){
    return (pow(velocity, 2)/9.81) * 2 * sin(theta)
}

#vf = vi + at
final_velocity(vi, a, t){
    return vi + a * t
}

#d = vit + 1/2 at^2
distance(vi, a, t){
    return vi + a * t
}
#vf^2 = vi^2 + 2ad
initial_velocity(x, vf, a){
    return sqrt(pow(vf, 2) - 2 * a * x)
}

#d = 1/2(vf + vi)t
distance2(vi, vf, t){
    return (vf + vi) * t / 2
}
#centr. acc = v^2/r
centripetal_acceleration(v, r){
    return pow(v, 2)/r
}

#period = 2pir/v
period(v, r){
    return 2 * 3.14 / v
}
