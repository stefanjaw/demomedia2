# -*- coding: utf-8 -*-

from odoo import models, fields, api
import hashlib 
import logging
_logger = logging.getLogger(__name__)

class AccountJournal(models.Model):
    _inherit = 'account.journal'
    
    micr_enable = fields.Boolean()
    
    company_registry = fields.Char(related='company_id.company_registry')
    company_name = fields.Char(related='company_id.name')
    #po_box = fields.Char()
    company_po_box = fields.Char()
    company_city = fields.Char(related='company_id.city')
    company_state_code = fields.Char(related='company_id.state_id.code')
    company_zip = fields.Char(related='company_id.zip')
    
    bank_name = fields.Char(related='bank_id.name')
    bank_bic = fields.Char(related='bank_id.bic')
    bank_street = fields.Char(related='bank_id.street')
    bank_street2 = fields.Char(related='bank_id.street2')
    bank_city = fields.Char(related='bank_id.city')
    bank_state_code = fields.Char(related='bank_id.state.code')
    bank_zip = fields.Char(related='bank_id.zip')
    bank_account_aba_routing = fields.Char(related='bank_account_id.aba_routing')
    bank_account_number = fields.Char(related='bank_account_id.acc_number')
    
    micr_letters = [
        ('code_a', 'A'),
        ('code_b', 'B'),
        ('code_c', 'C'),
        ('code_d', 'D'),
    ]
    micr_f1 = fields.Selection( micr_letters, copy=False, index=True, default='code_c')
    micr_f2 = fields.Selection( micr_letters, copy=False, index=True, default='code_c')
    micr_f3 = fields.Selection( micr_letters, copy=False, index=True, default='code_a')
    micr_f4 = fields.Selection( micr_letters, copy=False, index=True, default='code_a')
    micr_f5 = fields.Selection( micr_letters, copy=False, index=True, default='code_c')
    
    check_sequence_size = fields.Integer(
        related='check_sequence_id.padding', readonly=False)
    check_sequence_next_number = fields.Integer(
        related='check_sequence_id.number_next_actual', readonly=False )
    
    hash_code = fields.Char(string='hash', compute="create_hash_code", readonly=False, store=True)#readonly=True)

    @api.model
    def default_get(self):
        _logger.info("==========DEB46: DEFAULT GET")
    
    '''
    hash_fields = [ "company_registry", "company_name", "po_box", "company_city", "company_state_code", "company_zip",
                    "bank_name", "bank_bic", "bank_street", "bank_street2", "bank_city", "bank_state_code", "bank_zip",
                    "bank_account_aba_routing","bank_account_number"]
    '''
    hash_fields = [ "company_registry", "company_name", "po_box" ]
    
    '''
    @api.onchange( 'hash_code' )
    def test(self):
        _logger.info("==========DEB52: HASH CODE ON CHANGE %s", self.hash_code)
        return {
            'warning': {
                'title': 'Warning!',
                'message': 'The warning text'
            }
        }
    '''
    
    '''
    def create_hash_code(self):
        if self.micr_enable:
            data = ''
            old_hash_code = self.hash_code
            _logger.info("=====DEB68 OLD HASH CODE: %s", old_hash_code)
            for field in self.hash_fields:
                _logger.info("=====DEB70 VALUES: %s", eval( "self.{}".format(field) ) )
                if eval( "self.{}".format(field) ):
                    _logger.info("=====DEB72 FIELD %s, VALUES: %s", field, eval( "self.{}".format(field) ) )
                    data = data + "{}=".format(field) + eval( "self.{}".format(field) ) + "."
            _logger.info("=====DEB55 EJECUTO EL CREATE HASH CODE")
            data = hashlib.md5( data.encode() ).hexdigest()
            if data != old_hash_code:
                self.hash_code = data
                self.write( { 'hash_code' : data })
                _logger.info("=====DEB68 DIFERENTE NEEWW HASH CODE: %s", self.hash_code)
                return self.hash_code
            #self.write( { 'po_box' : 'XYZ1' })
            #self.hash_code = data
            #return self.hash_code
    '''
    
    '''
    @api.model
    def create(self, vals):
        res = super(AccountJournal,self).create(vals)
        hash_code = self.create_hash_code()
        self.update({ 'hash_code' : self.hash_code })
        self.log_in_chatter(self.hash_code)
        return res
    '''

    '''
    def write(self, vals):
        _logger.info('vals to write \n{}'.format(vals))
        hash_code = self.create_hash_code()
        if self.hash_code != hash_code:
            vals['hash_code'] = self.hash_code
            self.log_in_chatter( self.hash_code)
        res = super(AccountJournal, self).write(vals)
        return res
    '''
    
    '''
    def log_in_chatter(self,body):
        chatter = self.env['mail.message']
        chatter.create({
                        'res_id': self.id,
                        'model':'account.journal',
                        'body': body,
                       })
    '''
