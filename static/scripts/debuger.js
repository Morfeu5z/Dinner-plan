function log(mess, type = 'd') {
    if (localStorage.getItem('debuger') == 'true') {
        switch (type) {
            case 'd':
                console.log('Debug: ' + mess);
                break;
            case 'cp':
                console.log('Control point: ' + mess);
                break;
            case 'i':
                console.log('Info: ' + mess);
                break;
            case 'r':
                console.log('Run: ' + mess);
                break;
            case 'l':
                console.log('Loaded: ' + mess);
                break;
            case 'c':
                console.log('Clicked: ' + mess);
                break;
            case 'gt':
                console.log('Go to: ' + mess);
                break;
            default:
                console.log('Debug: ' + mess)
        }
    }
}
