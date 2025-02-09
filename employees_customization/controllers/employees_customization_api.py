from odoo import http
from odoo.http import request
import json


class EmployeeCustomizationsControllerApi(http.Controller):

    @http.route('/api/set_overtime', type='json', auth='public', methods=['POST'])
    def set_overtime(self):
        payload = json.loads(request.httprequest.data.decode())
        employee_id = payload.get('employee_id')
        overtime = payload.get('overtime')
        employee = request.env['hr.employee'].sudo().search([('id', '=', int(employee_id))], limit=1)
        if employee:
            employee.sudo().write({'overtime_ability': bool(overtime)})
            return {'success': True, 'message': 'Overtime ability updated successfully'}
        return {'success': False, 'message': 'Employee not found'}

    @http.route('/api/get_overtime', type='http', auth='public', methods=['GET'])
    def get_overtime(self, employee_id):
        employee = request.env['hr.employee'].sudo().search([('id', '=', int(employee_id))], limit=1)
        if employee:
            return json.dumps({'success': True, 'overtime_ability': employee.overtime_ability})
        return json.dumps({'success': False, 'message': 'Employee not found'})
