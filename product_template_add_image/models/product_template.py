from openerp import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # Binary image fields.
    additional_image_1 = fields.Binary('Product Image 1')
    additional_image_2 = fields.Binary('Product Image 2')
    additional_image_3 = fields.Binary('Product Image 3')
    additional_image_4 = fields.Binary('Product Image 4')
    additional_image_5 = fields.Binary('Product Image 5')
    # Filestore images.
    filestore_images = fields.Many2many(
        comodel_name="ir.attachment",
        relation="product_template_ir_attachment_rel",
        column1="product_template_id",
        column2="attachment_id",
        string="Attachments",
    )
