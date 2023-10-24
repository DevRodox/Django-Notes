from django.test import TestCase
from django.urls import reverse
from .models import Note

class NoteTestCase(TestCase):
    def setUp(self):
        self.note = Note.objects.create(title="Nota de prueba", content="Contenido de prueba")

    def test_creacion_nota(self):
        nueva_nota = Note.objects.create(title="Nueva Nota", content="Contenido de la nueva nota")
        self.assertEqual(nueva_nota.title, "Nueva Nota")
        self.assertEqual(nueva_nota.content, "Contenido de la nueva nota")

    def test_actualizacion_nota(self):
        url = reverse('mynotes:note_edit', args=[self.note.id])
        response = self.client.post(url, {'title': 'Nota Actualizada', 'content': 'Contenido actualizado'})
        self.assertEqual(response.status_code, 302)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Nota Actualizada')
        self.assertEqual(self.note.content, 'Contenido actualizado')

    def test_visualizacion_detalle_nota(self):
        url = reverse('mynotes:note_detail', args=[self.note.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nota de prueba')
        self.assertContains(response, 'Contenido de prueba')
        self.assertContains(response, 'Fecha de Creación')

    def test_eliminar_nota(self):
        url = reverse('mynotes:note_delete', args=[self.note.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        with self.assertRaises(Note.DoesNotExist):
            self.note.refresh_from_db()

    def test_carga_lista_de_notas(self):
        url = reverse('mynotes:note_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nota de prueba')
        self.assertContains(response, 'Contenido de prueba')





