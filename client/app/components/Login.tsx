import React, { FunctionComponent } from 'react';
import { Container, Content, Form, Item, Input } from 'native-base';

type LoginProps = {};

const Login: FunctionComponent<LoginProps> = (props: LoginProps) => {
  return (
    <Container>
      <Content padder>
        <Form>
          <Item rounded>
            <Input style={styles.input} placeholder="Username" />
          </Item>
          <Item rounded>
            <Input placeholder="Password" />
          </Item>
        </Form>
      </Content>
    </Container>
  );
};

const styles: StyleSheet = StyleSheet.create({
  input: {
    marginTop: 16,
  },
});

export default Login;
