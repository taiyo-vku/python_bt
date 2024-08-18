def main():
   
    Ta = float(input('Nhap nhiet do khong khi (°C): '))
    V = float(input('Nhap toc do gio (km/h): '))

    WCI = WCI = 13.12 + 0.6215 * Ta - 11.37 * (V ** 0.16) + 0.3965 * Ta * (V ** 0.16)

    WCI = round(WCI)

    print(f'Chi so gio lanh (WCI) la {WCI}')



if __name__ == '__main__':
    main()