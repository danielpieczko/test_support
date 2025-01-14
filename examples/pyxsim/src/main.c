#include <print.h>
#include <xcore/port.h>

int main() {
    port_t p0 = XS1_PORT_1G;
    port_enable(p0);
    port_out(p0, 1);
    printstrln("Hello World!");
    return 0;
}
