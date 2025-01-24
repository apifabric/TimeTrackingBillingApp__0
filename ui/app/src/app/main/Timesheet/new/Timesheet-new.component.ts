import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Timesheet-new',
  templateUrl: './Timesheet-new.component.html',
  styleUrls: ['./Timesheet-new.component.scss']
})
export class TimesheetNewComponent {
  @ViewChild("TimesheetForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}