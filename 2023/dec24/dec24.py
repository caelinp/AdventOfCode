import sympy as sp
def count_valid_intersections(hail):
    valid = 0
    test_area = (200000000000000, 400000000000000)
    for i in range(len(hail) - 1):
        p1, v1 = hail[i][0][:2], hail[i][1][:2]
        m1 = v1[1] / v1[0]
        b1 = p1[1] - m1 * p1[0]
        for j in range(i + 1, len(hail)):
            p2, v2 = hail[j][0][:2], hail[j][1][:2]
            m2 = v2[1] / v2[0]
            b2 = p2[1] - m2 * p2[0]
            if m1 == m2:
                if b1 == b2:
                    valid += 1
                else:
                    continue
            xi = (b2 - b1) / (m1 - m2)
            yi = m1 * xi + b1
            if test_area[0] <= xi <= test_area[1] and test_area[0] <= yi <= test_area[1]:
                t1 = (xi - p1[0]) / v1[0]
                t2 = (xi - p2[0]) / v2[0]
                if t1 >= 0 and t2 >= 0:
                    valid += 1
    return valid
def get_rock_start_pos(hail):
    # Define symbols
    rpx, rpy, rpz = sp.symbols("rpx, rpy, rpz", real=True)
    rvx, rvy, rvz = sp.symbols("rvx, rvy, rvz", real=True)
    t1, t2, t3 = sp.symbols("t1, t2, t3", real=True)
    # only need to find collisions with three different hailstones to solve for the 6 unknowns asked for in the question
    # each hailstone n we look at gives us one more unknown, the time of collision tn
    # so total unknowns for our system of equations is rpx, rpy, rpz, rvx, rvy, rvz, t1, t2, t3 (9 unknowns total)
    px1, py1, pz1 = hail[0][0]
    vx1, vy1, vz1 = hail[0][1]
    px2, py2, pz2 = hail[1][0]
    vx2, vy2, vz2 = hail[1][1]
    px3, py3, pz3 = hail[2][0]
    vx3, vy3, vz3 = hail[2][1]
    # Define the system of equations. need 9 equations for 9 unknowns
    equations = []
    equations.append(sp.Eq(rpx + rvx * t1, px1 + vx1 * t1))
    equations.append(sp.Eq(rpy + rvy * t1, py1 + vy1 * t1))
    equations.append(sp.Eq(rpz + rvz * t1, pz1 + vz1 * t1))
    equations.append(sp.Eq(rpx + rvx * t2, px2 + vx2 * t2))
    equations.append(sp.Eq(rpy + rvy * t2, py2 + vy2 * t2))
    equations.append(sp.Eq(rpz + rvz * t2, pz2 + vz2 * t2))
    equations.append(sp.Eq(rpx + rvx * t3, px3 + vx3 * t3))
    equations.append(sp.Eq(rpy + rvy * t3, py3 + vy3 * t3))
    equations.append(sp.Eq(rpz + rvz * t3, pz3 + vz3 * t3))
    # Solve the system of equations
    return sp.solve(equations, [rpx, rpy, rpz, rvx, rvy, rvz, t1, t2, t3])[0][:3]
hail = [[tuple(int(val) for val in vals.split(', ')) for vals in row.split(' @ ')] for row in open('input.txt').read().splitlines()]
p1 = count_valid_intersections(hail)
p2 = sum(get_rock_start_pos(hail))
print("part 1: {}\npart 2: {}".format(p1, p2))