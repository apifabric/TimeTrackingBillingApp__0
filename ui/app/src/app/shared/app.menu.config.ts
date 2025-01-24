import { MenuRootItem } from 'ontimize-web-ngx';

import { ClientCardComponent } from './Client-card/Client-card.component';

import { InvoiceCardComponent } from './Invoice-card/Invoice-card.component';

import { PaymentCardComponent } from './Payment-card/Payment-card.component';

import { PersonCardComponent } from './Person-card/Person-card.component';

import { ProjectCardComponent } from './Project-card/Project-card.component';

import { TaskCardComponent } from './Task-card/Task-card.component';

import { TimesheetCardComponent } from './Timesheet-card/Timesheet-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Client', name: 'CLIENT', icon: 'view_list', route: '/main/Client' }
    
        ,{ id: 'Invoice', name: 'INVOICE', icon: 'view_list', route: '/main/Invoice' }
    
        ,{ id: 'Payment', name: 'PAYMENT', icon: 'view_list', route: '/main/Payment' }
    
        ,{ id: 'Person', name: 'PERSON', icon: 'view_list', route: '/main/Person' }
    
        ,{ id: 'Project', name: 'PROJECT', icon: 'view_list', route: '/main/Project' }
    
        ,{ id: 'Task', name: 'TASK', icon: 'view_list', route: '/main/Task' }
    
        ,{ id: 'Timesheet', name: 'TIMESHEET', icon: 'view_list', route: '/main/Timesheet' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    ClientCardComponent

    ,InvoiceCardComponent

    ,PaymentCardComponent

    ,PersonCardComponent

    ,ProjectCardComponent

    ,TaskCardComponent

    ,TimesheetCardComponent

];