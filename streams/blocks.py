from wagtail.core import blocks


class TitleAndTextBlock(blocks.StructBlock):
   
    # title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.TextBlock(required=True, help_text="Add additional text")
    subtitle =  blocks.CharBlock(required=True, help_text="Add your subtitle")

    class Meta:  
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"

class RichtextBlock(blocks.RichTextBlock):

    class Meta:  # noqa
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "Full RichText"        
